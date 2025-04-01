# ctis-simulator
Simulate a Computed Tomography Imaging Spectrometer image from a 3D hyperspectral cube.

Input : A 3D image (preferably in the form of a .tiff file) representing a hyperspectral cube of an object.
Output : A 2D image (.png) representing the CTIS acquisition of that object.

<br/>

![ctis](ressources/ims_for_readme/ctis_autocrop.png)

(image modified from Wikipedia)
<br/>

___
### Usage 
MWE :  
```
python main.py -I <input directory with hyperspectral cubes> -O <output directory for CTIS images>  
```
to try it out with the example cube from this repo :  
```
python main.py -I ressources/input_cubes_small -O .
```

Customization :  

   
* Change CTIS geometries with ```--grating```, ```--min_wavelength```, ```--max_wavelength```.
 ![ctis](ressources/ims_for_readme/geoms.png)
* Change spectral sensitivity of the sensor by providing a csv defining it. An example is at [ressources/spectral_sensitivity.csv](ressources/spectral_sensitivity.csv). 
* Chose whether you're providing a hyperspectral cube or the intermediary cube directly with ```--field_stop```
* The CTIS action can be modelized by a matrix S between the reduced hyperspectral cube and the CTIS image. This matrix can be computed with ```--compute_system_matrix```. It can be useful for reconstruction approaches. Note however that the computation time can be quite long.

### Flags and Arguments

- `-I`, `--input_dir` (required): Specifies the input directory containing hyperspectral cubes in TIFF format.
- `-O`, `--output_dir` (required): Specifies the output directory where the CTIS images will be saved.
- `-o0`, `--o0_attenuator`: Sets the attenuation coefficient of the 0th order. Default is `0.1`.
- `-g`, `--gain`: Sets the gain of the CCD. Default is `50`.
- `-w_min`, `--min_wavelength`: Sets the minimum wavelength of the hyperspectral cube. Default is `400`.
- `-w_max`, `--max_wavelength`: Sets the maximum wavelength of the hyperspectral cube. Default is `1000`.
- `-s`, `--spectral_sensitivity`: Specifies the path to a CSV file defining the spectral sensitivity of the sensor.
- `-gr`, `--grating`: Sets the grating geometry. This argument must be of the form `<1|2><R|C|H><even positive int less than 116>`. Default is `1R60`.
- `-l`, `--fpa_length`: Sets the length of the CTIS image. Default is `512`.
- `-m`, `--compute_system_matrix`: If set, the system matrix representing the CTIS action will be computed. This can be very long.
- `-fs`, `--field_stop`: If set, the script will apply an objective lens and a field stop to reduce the cube.
- `-v`, `--verbose`: If set, the script will print additional information during execution.

### Example Usage

To customize the CTIS geometries and other parameters:

```sh
python main.py -I <input directory> -O <output directory> -o0 0.2 -g 60 -w_min 450 -w_max 950 -s ressources/spectral_sensitivity.csv -gr 2H80 -l 600 -m -fs -v
```

This command sets various parameters such as the attenuation coefficient, gain, wavelength range, spectral sensitivity, grating geometry, FPA length, and enables the computation of the system matrix, field stop effect, and verbose mode.

___
### Bibliography 

* The CTIS system is from :  *Computed-tomography imaging spectrometer: experimental calibration and reconstruction results*, Descour et al, Applied Optics (1995) 
([pdf](https://pdfs.semanticscholar.org/c886/1e02bbcb5a513927361b31223c7618d99dac.pdf))  
* The diffraction grating geometries we implemented come from : *Maximizing the resolution of a CTIS instrument*, Hagen et al, Imaging Spectrometry (2006) ([pdf](https://www.researchgate.net/profile/Nathan_Hagen/publication/228476247_Maximizing_the_resolution_of_a_CTIS_instrument_-_art_no_63020L/links/00b4952b33e7c72e1e000000/Maximizing-the-resolution-of-a-CTIS-instrument-art-no-63020L.pdf))