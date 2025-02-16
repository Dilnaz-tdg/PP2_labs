
import json

with open(r"C:\Users\Aspire 3\Desktop\PP2_labs\lab4\sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("DN", " " * 49, "Description", " "*11,  "Speed", " " * 4, "MTU")
print("-" * 50, " ",  "-" * 20, " "*2,  "-" * 6, " "*2 , "-" * 6)

for item in data["imdata"]:
    attributes = item.get("l1PhysIf", {}).get("attributes", {})
    
    dn = attributes.get("dn", "")
    description = attributes.get("descr", "")  
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "")

    print(f"{dn:<50} {description:<25} {speed:<10} {mtu:<6}") 