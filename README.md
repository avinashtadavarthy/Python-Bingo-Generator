# Python-Bingo-Generator
A command-line tool to generate unlimited printable bingo tickets on your PC !

## What does it do?
This tool generates as many bingo tickets as we want as high-quality, printable PNGs. It is based on the Pillow (PIL) Imaging Library.

## How to use it?
### Step 1
Install Pillow from pip by running the following the instructions from the [official website](https://pillow.readthedocs.io/en/stable/installation.html).

### Step 2
- Clone the repository onto your local machine.
- Navigate to a folder where you would like to generate the tickets.
- Run the 'generator.py' file in that directory.
```
python3 generator.py --seed <any random number> --tickets <number of tickets required>
```

## Example
- To test the program, once the repository has been cloned, execute the following:
```
python3 generator.py --seed 495434 --tickets 10
```
- This would create 10 bingo tickets and would store the compressed images in a subfolder called ```/bingotickets```.

## Example Ticket

## Note
This project is still under development and will get much smarter over time. This was only an attempt to make a utility to automate the mundane task of searching for BINGO ticket generators online.
