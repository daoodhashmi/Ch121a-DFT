from pathlib import Path

text = Path("water.out").read_text()

# Extract total energy from ORCA output
for line in text.splitlines():
    if "FINAL SINGLE POINT ENERGY" in line:
        energy_hartree = float(line.split()[-1])
        print(f"Total HF energy: {energy_hartree:.12f} Hartree")
        print(f"Total HF energy: {energy_hartree * 27.2114:.4f} eV")
        break
else:
    print("Could not find final energy.")
