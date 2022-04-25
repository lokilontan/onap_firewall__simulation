import time

class VFirewall:
    """ Simulates traffic filtering(not going to implement this)
        and sends data to the consumer(std out)

        Communicates with ONAP every two seconds. 
        Sends info about the rate
    """
    def __init__(self):
        self.packet_counter = 0
        self.time_current = time.time()
        self.period_counter = 0

    def accept(self, packet: str) -> None:
        """ LOG's the packet to the std out
            Adjusts the counter variable for the future rates measurements

        Args:
            str: accepted packet

        Returns:
            None
        """
        print("LOG: VFirewall - Packet received:", packet)
        self.packet_counter += 1
        
    def updateMetrics(self, onap) -> None:
        """ Every 2 seconds calculates the rate.
            Sends it to the ONAP module

        Args:
            Onap: for communication with the onap module

        Returns:
            None
        """
        #Check if 2 seconds passed
        diff = int(time.time() - self.time_current)
        if (diff%2 == 0) and (diff/2 != self.period_counter) :
            self.period_counter = diff/2
            rate_measured = self.packet_counter/2
            self.packet_counter = 0
            
            #Send the measured rate to ORAN for update
            onap.collectRate(rate_measured)
             
            