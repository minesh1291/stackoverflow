- Update & upgrade
```bash
sudo apt update
sudo apt upgrade -y
```

- System information
```bash
uname -a
# Linux ubuntu-vm-2 5.3.0-1032-gcp #34~18.04.1-Ubuntu SMP Tue Jul 14 22:07:36 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
sudo lshw  # hardware information
```

- Disable touch screen on ubuntu 18.04 xps 15 
```bash
xinput --list  # your touchscreen XID
xinput disable [touchscreen XID]
```

- System restart
```bash
sudo reboot
```

- Create tar archive
```bash
tar -zcvf tar-archive-name.tar.gz source-folder-name
```

- Start VNC Server
```bash
#vncserver -localhost no -geometry 3200x1800 -depth 16 # for hi-res
vncserver -localhost no -geometry 1900x1100 -depth 16
```

- Download from site path 
```bash
wget -xr -np <site path>
```

- Download Manager
```bash
# Xtreme Download Manager (XDM)
sudo add-apt-repository ppa:noobslab/apps
sudo apt-get update
sudo apt-get install xdman

# uGet
sudo add-apt-repository ppa:plushuang-tw/uget-stable
sudo apt-get update
sudo apt-get install uget

# MultiGet
sudo apt-get install multiget
```
  
- Restart pulseaudio and alsa
```bash
pulseaudio -k
sudo alsa force-reload
pulseaudio --start
```

- GPU Information
```
$sudo apt install clinfo
$clinfo

Number of platforms                               1
  Platform Name                                   Clover
  Platform Vendor                                 Mesa
  Platform Version                                OpenCL 1.1 Mesa 13.0.6
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd
  Platform Extensions function suffix             MESA

  Platform Name                                   Clover
Number of devices                                 1
  Device Name                                     NVC4
  Device Vendor                                   NVIDIA
  Device Vendor ID                                0x10de
  Device Version                                  OpenCL 1.1 Mesa 13.0.6
  Driver Version                                  13.0.6
  Device OpenCL C Version                         OpenCL C 1.1 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Max compute units                               7
  Max clock frequency                             512MHz
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x64
  Max work group size                             1024
=== CL_PROGRAM_BUILD_LOG ===
invalid source  Preferred work group size multiple              invalid source
  Preferred / native vector sizes                 
    char                                                16 / 16      
    short                                                8 / 8       
    int                                                  4 / 4       
    long                                                 2 / 2                  
    half                                                 0 / 0        (n/a)     
    float                                                4 / 4                  
    double                                               2 / 2        (cl_khr_fp64)                                                                             
  Half-precision Floating-point support           (n/a)                         
  Single-precision Floating-point support         (core)                        
    Denormals                                     No                            
    Infinity and NANs                             Yes                           
    Round to nearest                              Yes                           
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              1099511627776 (1024GiB)
  Error Correction support                        No
  Max memory allocation                           1099511627776 (1024GiB)
  Unified memory for Host and Device              Yes
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        None
  Image support                                   No
  Local memory type                               Local
  Local memory size                               49152 (48KiB)
  Max constant buffer size                        65536 (64KiB)
  Max number of constant args                     15
  Max size of kernel argument                     4096 (4KiB)
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Profiling timer resolution                      0ns
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
  Device Available                                Yes
  Compiler Available                              Yes
  Device Extensions                               cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_byte_addressable_store cl_khr_fp64

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  Clover
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [MESA]
  clCreateContext(NULL, ...) [default]            Success [MESA]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 Clover
    Device Name                                   NVC4
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 Clover
    Device Name                                   NVC4

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.2.11
  ICD loader Profile                              OpenCL 2.1
```
