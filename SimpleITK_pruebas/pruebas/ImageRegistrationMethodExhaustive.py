"""
This script demonstrates the use of the Exhaustive optimizer in the
ImageRegistrationMethod to estimate a good initial rotation position.

Because gradient descent base optimization can get stuck in local
minima, a good initial transform is critical for reasonable
results. Search a reasonable space on a grid with brute force may be a
reliable way to get a starting location for further optimization.

The initial translation and center of rotation for the transform is
initialized based on the first principle moments of the intensities of
the image. Then in either 2D or 3D a Euler transform is used to
exhaustively search a grid of the rotation space at a certain step
size. The resulting transform is a reasonable guess where to start
further registration.
"""

from __future__ import print_function
from __future__ import division


import SimpleITK as sitk
from PIL import Image
import sys
import os
from math import pi


def command_iteration(method):
    if method.GetOptimizerIteration() == 0:
        print("Scales: ", method.GetOptimizerScales())
    print("{0:3} = {1:7.5f} : {2}".format(
                                            method.GetOptimizerIteration(),
                                            method.GetMetricValue(),
                                            method.GetOptimizerPosition()
                                            )
          )


fixed_file = '../images/fixedImage.png'
moving_file = '../images/movingImage.png'

fixed = sitk.ReadImage(fixed_file, sitk.sitkFloat32)

moving = sitk.ReadImage(moving_file, sitk.sitkFloat32)

R = sitk.ImageRegistrationMethod()

R.SetMetricAsMattesMutualInformation(numberOfHistogramBins=50)

sample_per_axis = 50
tx = None
if fixed.GetDimension() == 2:
    tx = sitk.Euler2DTransform()
    # Set the number of samples (radius) in each dimension, with a
    # default step size of 1.0
    R.SetOptimizerAsExhaustive([sample_per_axis//2, 0, 0])
    # Utilize the scale to set the step size for each dimension
    R.SetOptimizerScales([2.0*pi/sample_per_axis, 1.0, 1.0])
elif fixed.GetDimension() == 3:
    tx = sitk.Euler3DTransform()
    R.SetOptimizerAsExhaustive([sample_per_axis//2, sample_per_axis//2, sample_per_axis//4, 0, 0, 0])
    R.SetOptimizerScales([2.0*pi/sample_per_axis, 2.0*pi/sample_per_axis, 2.0*pi/sample_per_axis, 1.0, 1.0, 1.0])

# Initialize the transform with a translation and the center of
# rotation from the moments of intensity.
tx = sitk.CenteredTransformInitializer(fixed, moving, tx)

R.SetInitialTransform(tx)

R.SetInterpolator(sitk.sitkLinear)

R.AddCommand(sitk.sitkIterationEvent, lambda: command_iteration(R))

outTx = R.Execute(fixed, moving)

print("-------")
print(outTx)
print("Optimizer stop condition: {0}".format(R.GetOptimizerStopConditionDescription()))
print(" Iteration: {0}".format(R.GetOptimizerIteration()))
print(" Metric value: {0}".format(R.GetMetricValue()))


# sitk.WriteTransform(outTx,  sys.argv[3])

if not "SITK_NOSHOW" in os.environ:

    resampler = sitk.ResampleImageFilter()
    resampler.SetReferenceImage(fixed)
    resampler.SetInterpolator(sitk.sitkLinear)
    resampler.SetDefaultPixelValue(1)
    resampler.SetTransform(outTx)

    out = resampler.Execute(moving)

    simg1 = sitk.Cast(sitk.RescaleIntensity(fixed), sitk.sitkUInt8)
    simg2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)
    cimg = sitk.Compose(simg1, simg2, simg1//2.+simg2//2.)

    nda = sitk.GetArrayViewFromImage(cimg)
    my_pil = Image.fromarray(nda)
    my_pil.show()

    # sitk.Show(cimg, "ImageRegistrationExhaustive Composition")
