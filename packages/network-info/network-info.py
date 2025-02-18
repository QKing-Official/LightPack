import os
import sys
import platform
import psutil
import subprocess

def get_network_info():
    """Gather network information."""
    info = {
        "System": platform.system(),
        "Hostname": platform.node(),
        "Interfaces": {}
    }

    # Get network interfaces and their details
    if_addrs = psutil.net_if_addrs()
    for interface, addrs in if_addrs.items():
        info["Interfaces"][interface] = []
        for addr in addrs:
            addr_info = {
                "Family": addr.family.name,
                "Address": addr.address,
                "Netmask": addr.netmask if addr.netmask else "N/A",
                "Broadcast": addr.broadcast if addr.broadcast else "N/A"
            }
            info["Interfaces"][interface].append(addr_info)

    # Get network interface statistics
    net_io = psutil.net_io_counters(pernic=True)
    for interface, stats in net_io.items():
        if interface in info["Interfaces"]:
            info["Interfaces"][interface].append({
                "Bytes Sent": stats.bytes_sent,
                "Bytes Received": stats.bytes_recv,
                "Packets Sent": stats.packets_sent,
                "Packets Received": stats.packets_recv,
                "Errors": stats.errin + stats.errout,
                "Dropped": stats.dropin + stats.dropout
            })

    return info

def display_info():
    """Print network information in a readable format."""
    print("\n--- Network Information ---")
    info = get_network_info()
    for key, value in info.items():
        if key == "Interfaces":
            print(f"{key}:")
            for iface, details in value.items():
                print(f"  {iface}:")
                for detail in details:
                    for k, v in detail.items():
                        print(f"    {k}: {v}")
        else:
            print(f"{key}: {value}")

if __name__ == "__main__":
    display_info()
