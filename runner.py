import subprocess
import pandas as pd
import matplotlib.pyplot as plt


def process(language: str, compiler_call: str) -> str:
    data_file_path = f"./{language}_resolution/data.csv"
    # create empty data file
    with open(data_file_path, "w") as data_file:
        data_file.write("")
        data_file.close()

    compile = subprocess.call(
        compiler_call,
        shell=True,
    )

    if compile != 0:
        raise RuntimeError(f"Couldnt compile {language} file")

    with open(data_file_path, "a") as data_file:
        size = 1
        while size < 15000:
            ret_code = subprocess.call(
                [f"./{language}_resolution/resolution", str(size)], stdout=data_file
            )
            size = size * 2
        subprocess.call(
            [f"./{language}_resolution/resolution", str(15000)], stdout=data_file
        )
    return data_file_path


def main():
    # First, run C solution
    data_file_path = process(
        language="c",
        compiler_call="gcc -Wall -o ./c_resolution/resolution ./c_resolution/resolution.c",
    )
    plt.figure(0)
    # Then, run FORTRAN solution
    data_file_path = process(
        language="fortran",
        compiler_call="gfortran ./fortran_resolution/resolution.f95 -o ./fortran_resolution/resolution",
    )
    plt.figure(1)

if __name__ == "__main__":
    main()
