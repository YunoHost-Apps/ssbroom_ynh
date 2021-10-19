"""
script to cross-compile go-ssb-room for arm64 and other architectures

before running, run:
- sudo apt install gcc-aarch64-linux-gnu
- sudo apt install gcc-arm-linux-gnueabi

"""
import subprocess
import os

# path to project directory
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
WORKING_DIR = "/srv/build_ssbroom"
GIT_URL = "https://github.com/ssb-ngi-pointer/go-ssb-room.git"
OUTPUT_DIR = "/srv/files.commoninternet.net"


def pull_repo():
    if not os.path.exists(WORKING_DIR):
        subprocess.check_call(["git", "clone", GIT_URL, WORKING_DIR])
    else:
        subprocess.check_call(["git", "pull"], cwd=WORKING_DIR)


def crosscompile_go_ssb_room():
    subprocess.check_call(["git", "pull"], cwd=WORKING_DIR)
    print("[CROSS-COMPILING go-ssb-room/server]")
    subprocess.check_call(["env", "CGO_ENABLED=1", "CC=aarch64-linux-gnu-gcc",
                           "CC_FOR_TARGET=gcc-aarch64-linux-gnu", "GOOS=linux",
                           "GOARCH=arm64", "go", "build", "./cmd/server"], cwd=WORKING_DIR)
    print("[CROSS-COMPILING go-ssb-room/insert-user]")
    subprocess.check_call(["env", "CGO_ENABLED=1", "CC=aarch64-linux-gnu-gcc",
                           "CC_FOR_TARGET=gcc-aarch64-linux-gnu", "GOOS=linux",
                           "GOARCH=arm64", "go", "build", "./cmd/insert-user"], cwd=WORKING_DIR)
    publish(architecture="aarch64")

def crosscompile_go_ssb_room_for_arm7():
    subprocess.check_call(["git", "pull"], cwd=WORKING_DIR)
    print("[CROSS-COMPILING for arm7 go-ssb-room/server]")
    subprocess.check_call(["env", "CGO_ENABLED=1", "CC=arm-linux-gnueabi-gcc",
                           "GOOS=linux",
                           "GOARCH=arm", "GOARM=7", "go", "build", "./cmd/server"], cwd=WORKING_DIR)
    print("[CROSS-COMPILING for arm7 go-ssb-room/insert-user]")
    subprocess.check_call(["env", "CGO_ENABLED=1", "CC=arm-linux-gnueabi-gcc",
                           "GOOS=linux",
                           "GOARCH=arm", "GOARM=7", "go", "build", "./cmd/insert-user"], cwd=WORKING_DIR)
    publish(architecture="arm7")

def compile_go_ssb_room():
    subprocess.check_call(["git", "pull"], cwd=WORKING_DIR)
    print("[COMPILING go-ssb-room/server for amd64]")
    subprocess.check_call(["go", "build", "./cmd/server"], cwd=WORKING_DIR)
    print("[COMPILING go-ssb-room/insert-user for amd64]")
    subprocess.check_call(["go", "build", "./cmd/insert-user"], cwd=WORKING_DIR)
    publish(architecture="amd64")


def publish(architecture):
    subprocess.check_call(["mkdir", "-p", OUTPUT_DIR])
    binaries = ["insert-user", "server"]
    output_folder_name = "go-ssb-room_2.0.6_Linux_{}".format(architecture)
    output_folder_path = os.path.join(OUTPUT_DIR, output_folder_name)
    subprocess.check_call(["mkdir", "-p", output_folder_path])
    for binary in binaries:
        f_path = os.path.join(WORKING_DIR, binary)
        output_path = os.path.join(output_folder_path, binary)
        subprocess.check_call(["cp", f_path, output_path])
    # create a tar
    tar_path = output_folder_path + ".tar.gz"
    subprocess.check_call(["tar", "-czvf", tar_path, "-C", output_folder_path, "."])


if __name__ == '__main__':
    pull_repo()
    # crosscompile_go_ssb_room()
    crosscompile_go_ssb_room_for_arm7()
    # compile_go_ssb_room()
