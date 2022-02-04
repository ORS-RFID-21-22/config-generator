# Default profile
profile = {
    'dfeDataOutputMode' : {
        'modeType' :        1,
            # 1 - frame based chirps
            # 2 - continuous chirping
            # 3 - advanced frame config
            # only 1 and 3 are supported
    },
    'channelCfg' : {
        'rxChannelEn' :     15, # Receive antenna mask e.g for 4 antennas, it is 0x1111b = 15
        'txChannelEn' :     7,  # Transmit antenna mask
        'cascading' :       0   # SoC cascading, not applicable, set to 0
    },
    'adcCfg' : {
        'numADCBits' :      2, # Number of ADC bits (0 for 12-bits, 1 for 14-bits and 2 for 16-bits). Only 16-bit supported
        'adcOutputFmt' :    2 
            # 0 - real
            # 1 - complex 1x (image band filtered output)
            # 2 - complex 2x (image band visible))
            # only complex supported
    },
    'adcBufCfg' : {
        'subFrameIdx' :     -1,
            # For legacy mode, that field should be set to -1.
            # For advanced frame mode, it should be set to either theintended subframe number or
            # -1 to apply same config to all subframes.
        'adcOutputFmt' :    0,
            # ADCBUF out format
            # 0-Complex,
            # 1-Real
            # Only complex supported
        'sampleSwap' :      1,  # Only 1 supported
        'chanInterleave' :  1,  # Only 1 supported
        'chipThreshold' :   1
            # Chirp Threshold configuration used for ADCBUF buffer to trigger ping /pong buffer switch.
            # Valid values:
            # 0-8 for demos that use DSP for 1D FFT and LVDS streaming is disabled
            # only 1 for demos that use HWA for 1D FFT
    },
    'profileCfg' : {
        'profileId' :       0, 
        'startFreq' :       60, # "Frequency Start" in GHz (float values allowed)
        'idleTime' :        388,  # "Idle Time" in u-sec (float values allowed)
        'adcStartTime' :    7,  # "ADC Valid Start Time" in u-sec (float values allowed)
        'rampEndTime' :     28.49, # "Ramp End Time" in u-sec (float values allowed)
        'txOutPower' :      0,  # Tx output power back-off code for tx antennas (only 0 has been tested)
        'txPhaseShifter' :  0,  # tx phase shifter for tx antennas (only 0 has been tested)
        'freqSlopeConst' :  30, # "Frequency slope" for the chirp in MHz/usec (float values allowed)
        'txStartTime'    :  1,  # "TX Start Time" in u-sec (float values allowed)
        'numAdcSamples'  :  256, # number of ADC samples collected during "ADC Sampling Time"
        'digOutSampleRate': 12499, # ADC sampling frequency in ksps. (<numAdcSamples> / <digOutSampleRate> = "ADC Sampling Time")
        'hpfCornerFreq1' :  0, # HPF1 (High Pass Filter 1) corner frequency
        'hpfCornerFreq2' :  0, # HPF2 (High Pass Filter 2) corner frequency
        'rxGain' :          30 # OR'ed value of RX gain in dB and RF gain target (See mmwavelink doxgen for details)
    },
    'chirpCfg1' : {
        'chirpStartIdx' :   0,
        'chirpEndIdx' :     0,
        'profileId' :       0, # should match profileCfg -> profileId
        'startFreqVar' :    0, # start frequency variation in Hz (only 0 has been tested)
        'freqSlopeVar' :    0, # frequency slope variation in kHz/us (only 0 has been tested)
        'idleTimeVar' :     0, # idle time variation in us (only 0 has been tested)
        'adcStartTimeVar' : 0, # adc start time variation (only 0 has been tested)
        'txEnMask' :        1 # tx antenna enable mask (Tx2,Tx1) e.g (10)b = Tx2 enabled, Tx1 disabled.
        # Individual chirps should have either only one distinct Tx antenna enabled (MIMO) or same TX antennas 
        # should be enabled for all chirps
    },
    'chirpCfg2' : {
        'chirpStartIdx' :   1,
        'chirpEndIdx' :     1,
        'profileId' :       0, # should match profileCfg -> profileId
        'startFreqVar' :    0, # start frequency variation in Hz (only 0 has been tested)
        'freqSlopeVar' :    0, # frequency slope variation in kHz/us (only 0 has been tested)
        'idleTimeVar' :     0, # idle time variation in us (only 0 has been tested)
        'adcStartTimeVar' : 0, # adc start time variation (only 0 has been tested)
        'txEnMask' :        2 # tx antenna enable mask (Tx2,Tx1) e.g (10)b = Tx2 enabled, Tx1 disabled.
        # Individual chirps should have either only one distinct Tx antenna enabled (MIMO) or same TX antennas 
        # should be enabled for all chirps
    },
    'chirpCfg3' : {
        'chirpStartIdx' :   2,
        'chirpEndIdx' :     2,
        'profileId' :       0, # should match profileCfg -> profileId
        'startFreqVar' :    0, # start frequency variation in Hz (only 0 has been tested)
        'freqSlopeVar' :    0, # frequency slope variation in kHz/us (only 0 has been tested)
        'idleTimeVar' :     0, # idle time variation in us (only 0 has been tested)
        'adcStartTimeVar' : 0, # adc start time variation (only 0 has been tested)
        'txEnMask' :        4 # tx antenna enable mask (Tx2,Tx1) e.g (10)b = Tx2 enabled, Tx1 disabled.
        # Individual chirps should have either only one distinct Tx antenna enabled (MIMO) or same TX antennas 
        # should be enabled for all chirps
    },
    'frameCfg' : {
        'chirpStartIdx' :   0, # 0 - 511
        'chirpEndIdx'   :   2, # start idx - 511
        'numLoops':         16, # 1 - 255
        'numFrames' :       0, # 0 - 65535, 0 means infinite
        'framePeriodicity': 100, # ms
        'triggerSel' :      1, # trigger select: 1 for software trigger, 2 for hardware trigger. only 1 is supported
        'frameTriggerDelay':0 # ms
    },
    'lowPower' : {
        'dontCare' :        0, # Keep at 0
        'adcMode' :         0, 
            # 0x00 : Regular ADC mode
            # 0x01 : Low power ADC mode (Not supported for xwr6xxx devices)
    },
    'guiMonitor' : {
        'subFrameIdx' :     -1,
        'detectedObjects':  1,
        'logMagRange':      1, # log magnitude range
        'noiseProfile':     0,
        'rangeAzimuthHeatMap': 0,
        'rangeDopplerHeatMap': 0,
        'statsInfo' :       1
    },
    'cfarCfg1' : {
        'subFrameIdx' :     -1,
        'procDirection' :   0,
        'mode' :            2,
        'noiseWin' :        8,
        'guardLen' :        4,
        'divShift' :        3,
        'cyclicMode' :      0,
        'thresholdScale':   15.0, #db
        'peakGrouping':     0
    },
    'cfarCfg2' : {
        'subFrameIdx' :     -1,
        'procDirection' :   1,
        'mode' :            0,
        'noiseWin' :        4,
        'guardLen' :        2,
        'divShift' :        3,
        'cyclicMode' :      1,
        'thresholdScale':   15.0, #db
        'peakGrouping':     0
    },
    'multiObjBeamForming' : {
        'subFrameIdx' :     -1,
        'featureEnabled':   1,
        'threshold' :       0.5
    },
    'clutterRemoval' : {
        'subFrameIdx' :     -1,
        'enabled':          0
    },
    'calibDcRangeSig' : {
        'subFrameIdx' :     -1,
        'enabled' :         0,
        'negativeBinIdx':   -5,
        'positiveBinIdx':   8,
        'numAvg':           256
    },
    'extendedMaxVelocity' : {
        'subframeIdx':      -1,
        'enabled':          0
    },
    'compRangeBiasAndRxChanPhase' : {
        'rangeBias' :       0.0,
        'compensation' : [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0]
    },
    'measureRangeBiasAndRxChanPhase' : {
        'enabled' :         0,
        'targetDistance' :  1.5,
        'searchWin'      :  0.2
    },
    'CQRxSatMonitor' : {
        'profile' :         0,
        'satMonSel':        3,
        'priSliceDuration': 4,
        'numSlices' :       63,
        'rxChanMask':       0
    },
    'CQSigImgMonitor' : {
        'profile':          0,
        'numSlices':        127,
        'numSamplePerSlice': 4
    },
    'analogMonitor' : {
        'rxSaturation':     0,
        'sigImgBand':       0
    },
    'aoaFovCfg' : {
        'subframeIdx':      -1,
        'minAzimuthDeg':    -90,
        'maxAzimuthDeg':    90,
        'minElevationDeg':  -90,
        'maxElevationDeg':  90
    },
    'cfarFovCfg1' : {
        'subFrameIdx' :     -1,
        'procDirection':    0,
        'min':              0,
        'max':              100
    },
    'cfarFovCfg2' : {
        'subFrameIdx' :     -1,
        'procDirection':    1,
        'min':              -1,
        'max':              1.00
    }
}