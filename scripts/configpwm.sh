echo 0 > /sys/class/pwm/pwmchip0/export
echo 33333333 > /sys/class/pwm/pwmchip0/pwm0/period        # 30 fps in ns
echo  1000000 > /sys/class/pwm/pwmchip0/pwm0/duty_cycle    # 1 ms high time in ns
echo        1 > /sys/class/pwm/pwmchip0/pwm0/enable        # Turn on


