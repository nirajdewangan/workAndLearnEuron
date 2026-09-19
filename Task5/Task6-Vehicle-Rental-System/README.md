# Vehicle Rental System

A beginner-friendly mini vehicle rental application built using Python inheritance.

## Requirements Covered

- Parent class named `Vehicle`
- Vehicle number, brand, model, and rental price per day
- Child classes named `Car` and `Bike`
- Number of seats for Car
- Engine capacity for Bike
- `calculate_rent(days)` method
- Static rental-duration validation method
- Two Car objects and two Bike objects
- Complete rent calculations for all vehicles

## Inheritance Demonstration

- `Car` and `Bike` inherit from `Vehicle`.
- Both child classes use `super().__init__()` for common attributes.
- Both override `display_details()` and call the parent method with `super()`.
- Both inherit `calculate_rent()` without repeating its code.

## Project Structure

```text
vehicle-rental-system/
├── vehicle_rental.py
├── README.md
├── YOUTUBE_SCRIPT.md
├── sample_output.txt
└── youtube-thumbnail.png
```

## How to Run

Open a terminal in this folder and run:

```bash
python vehicle_rental.py
```

On some systems, use:

```bash
python3 vehicle_rental.py
```

## Inheritance Structure

```text
Vehicle
  |-- Car
  |-- Bike
```

## Author

Niraj Kumar Dewangan
