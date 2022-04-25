from onap import Onap
from trafficgenerator import TrafficGenerator
from vfirewall import VFirewall

INIT_DELAY_COEF = 0.5
TARGET_RATE = 3 #packets/sec
THRESH_RANGE_LOW = 2.8 #packets/sec
THRESH_RANGE_HIGH = 3.2 #packets/sec

def main():
    trafficGenerator = TrafficGenerator(INIT_DELAY_COEF)
    firewall = VFirewall()
    onap = Onap(TARGET_RATE, THRESH_RANGE_LOW, THRESH_RANGE_HIGH)
    
    while True:
        #Traffic Generator sends the packet to firewall
        trafficGenerator.sendPacket(firewall)
        #Firewall determines the rates and sends the metrics to ONAP every 2 seconds
        firewall.updateMetrics(onap)
        #ONAP will check if the current measured rate is within the threshold range
        #If it is not then it will request TrafficGenerator to adjust the rate
        onap.adjustRate(trafficGenerator)

if __name__ == "__main__":
    main()

            