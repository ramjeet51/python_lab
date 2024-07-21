import subprocess

def scan_devices():
        try:
                    # Start the bluetoothctl process
                            process = subprocess.Popen(['bluetoothctl'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                                    
                                            # Enter the scan on command
                            process.stdin.write('scan on\n')
                            process.stdin.flush()
                                                                    
                            devices = set()
                            while True:
                                output = process.stdout.readline().strip()
                                if 'Device' in output:
                                    parts = output.split(' ', 2)
                                    if len(parts) >= 3:
                                                                                                                                                                                                                addr = parts[1]
                                                                                                                                                                                                                name = parts[2]
                                                                                                                                                                                                                devices.add((addr, name))
                                                                                                                                                                                                                print(f"Found device: {addr} - {name}")
                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                # Stop scanning after 10 seconds
                                                                                                                                                                                                    if 'discovery stopped' in output:
                                                                                                                                                                                                         break
                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                    # Stop the scan
                                                                                                                                                                                                    process.stdin.write('scan off\n')
                                                                                                                                                                                                    process.stdin.flush()
                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                    # Wait for the process to complete
                                                                                                                                                                                                    process.communicate()
                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                            return devices
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             except Exception as e:
                                                                                                                                                                                                                                                                                                                                                                print(f"Error: {e}")
                                                                                                                                                                                                                                                                                                                                                                return []

                                                                                                                                                                                                                                                                                                                                                    if _name_ == "_main_":
                                                                                                                                                                                                                                                                                                                                                        print("Scanning for Bluetooth devices...")
                                                                                                                                                                                                                                                                                                                                                        devices = scan_devices()
                                                                                                                                                                                                                                                                                                                                                        print(f"Found {len(devices)} devices.")
                                                                                                                                                                                                                                                                                                                                                        for addr, name in devices:
                                                                                                                                                                                                                                                                                                                                                             print(f"{addr} - {name}")
