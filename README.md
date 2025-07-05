# Device Model Converter

This repository includes a small C program, `device_model.c`, that reads a device name from standard input and prints the corresponding model using a fixed lookup table.

## Build

```bash
gcc device_model.c -o device_model
```

## Run

```bash
./device_model
```

### Example

Running the program and entering a known device name prints the model:

```bash
$ ./device_model
Enter device name: iPhone10,1
Model: iPhone 8
```
