'''
Created on Nov 21, 2013

@author: Jeffrey
'''

import usb.core
import usb.util

if __name__ == '__main__':
    print('hello')
    """
    dev = usb.core.find(find_all=True)
    # loop through devices, printing vendor and product ids in decimal and hex
    for cfg in dev:
        print('Decimal VendorID=' + str(cfg.idVendor) + ' & ProductID=' + str(cfg.idProduct))
        print('Hexadecimal VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct))
    
    """
    # find our device
    dev = usb.core.find(idVendor=0xd7d, idProduct=0x0100)
    
    # was it found?
    if dev is None:
        raise ValueError('Device not found')
    
    print('dev.bLength: ',dev.bLength)
    print('dev.bNumConfigurations: ',dev.bNumConfigurations)
    print('dev.bDeviceClass: ',dev.bDeviceClass)
    
    # set the active configuration. With no arguments, the first
    # configuration will be the active one
    dev.set_configuration()
    
    # get an endpoint instance
    cfg = dev.get_active_configuration()
    interface_number = cfg[(0,0)].bInterfaceNumber
    alternate_setting = usb.control.get_interface(dev,interface_number)
    intf = usb.util.find_descriptor(
        cfg, bInterfaceNumber = interface_number,
        bAlternateSetting = alternate_setting
    )
    
    ep = usb.util.find_descriptor(
        intf,
        # match the first OUT endpoint
        custom_match = \
        lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == \
            usb.util.ENDPOINT_OUT
    )
    
    assert ep is not None
    
    # write the data
    #ep.write('test')
    dev.write(1,'jeff',0)
    
    
    
    