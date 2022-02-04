from profile_dict import profile
import sys

# default
# start_frequency = 60            # GHz
# bandwidth = 3.5                 # GHz
# ramping_signal_slope = 70       # MHz/us
# adc_samples_per_chirp = 512     # 

# sampling_rate = 12499           # ksps

# ----------------------------------------------------------------------------
# Inputs
# ----------------------------------------------------------------------------
start_frequency = float(input('Start frequency (GHz): '))
bandwidth = float(input('Bandwidth (GHz): '))
ramping_signal_slope = float(input('Slope of ramping signal (MHz/us): '))
adc_samples_per_chirp = int(input('ADC samples per chirp: '))
sampling_rate = int(input('Sampling rate (ksps): '))

# ----------------------------------------------------------------------------
# Validations and Calculations
# ----------------------------------------------------------------------------
# adc_samples_per_chirp * 1000 / sampling_rate = sampling time in us
# end time = bandwidth * 1000 / ramping_signal_slope

# sampling end time <= ramp_end_time, so
# adcStartTime + adc_samples_per_chirp * 1000 / sampling_rate <= bandwidth * 1000 / ramping_signal_slope

# sampling end time * ramping_signal_slope / 1000 <= bandwidth
# adc_samples_per_chirp <= (sampling_rate * (ramp_end_time - adcStartTime)) / 1000
# ramping signal slope <= bandwidth * 1000 / adc_end_time 

ramp_end_time = bandwidth * 1000 / ramping_signal_slope
adc_sampling_time = round((adc_samples_per_chirp)/profile['profileCfg']['digOutSampleRate'] * 1000, 2)
adc_end_time = profile['profileCfg']['adcStartTime'] + adc_sampling_time

if (adc_end_time > ramp_end_time):
    sys.exit(
        f"ADC sampling end time ({adc_end_time} us) goes past ramp end time ({ramp_end_time} us). Decrease ADC samples per chirp, increase sampling "
        f"rate, decrease ramping signal slope, or increase bandwidth.\n\n"
        f"If keeping\n"
        f"  sampling rate = {sampling_rate}\n"
        f"  ramping signal slope = {ramping_signal_slope}\n"
        f"  bandwidth = {bandwidth}\n"
        f"The maximum ADC samples per chirp is {round((sampling_rate * (ramp_end_time - profile['profileCfg']['adcStartTime'])) / 1000, 2)}\n\n"
        f"If keeping \n"
        f"  sampling rate = {sampling_rate}\n"
        f"  ADC samples per chirp = {adc_samples_per_chirp}\n"
        f"  bandwidth = {bandwidth}\n"
        f"The maximum ramping signal slope is {round(bandwidth * 1000 / adc_end_time, 2)}\n\n"
        f"If keeping \n"
        f"  sampling rate = {sampling_rate}\n"
        f"  ramping signal slope = {ramping_signal_slope}\n"
        f"  ADC samples per chirp = {adc_samples_per_chirp}\n"
        f"The minimum bandwidth is {adc_end_time * ramping_signal_slope / 1000}\n"
    )

profile['profileCfg']['digOutSampleRate'] = sampling_rate
profile['profileCfg']['rampEndTime'] = ramp_end_time
profile['profileCfg']['freqSlopeConst'] = ramping_signal_slope
profile['profileCfg']['numAdcSamples'] = adc_samples_per_chirp

# ----------------------------------------------------------------------------
# Write to File
# ----------------------------------------------------------------------------
with open('profile.cfg', 'w') as f:
    # Write some header comments about profile
    f.write('% ---------------------------------------------------\n')
    f.write('% Starting frequency: ' + str(profile['profileCfg']['startFreq']) + ' GHz\n')
    f.write('% Bandwidth: ' + str(bandwidth) + ' GHz\n')
    f.write('% Ramping signal slope: ' + str(ramping_signal_slope) + ' MHz/us\n')
    f.write('% Ramp end time: ' + str(ramp_end_time) + ' us\n\n')

    f.write('% Sampling rate: ' + str(sampling_rate) + ' ksps\n')
    f.write('% ADC samples per chirp: ' + str(adc_samples_per_chirp) + '\n')
    f.write('% ADC sampling time: ' + str(profile['profileCfg']['adcStartTime']) + ' - ' + str(adc_end_time) + ' us\n')
    f.write('% ---------------------------------------------------\n\n')

    # Write profile commands
    f.write('sensorStop\n')
    f.write('flushCfg\n\n')

    for command in profile:
        f.write(''.join([i for i in command if not i.isdigit()]))
        for param in profile[command]:
            if type(profile[command][param]) == list:
                for item in profile[command][param]:
                    f.write(' ' + str(item))
            else:
                f.write(' ' + str(profile[command][param]))
        f.write('\n')

    f.write('\nsensorStart')

print('\nConfig written to profile.cfg\n')