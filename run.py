import time
import argparse
import os
import sys
import subprocess


def main():
    # defaults
    USE_GUI = True
    USE_FILESTREAM = True
    USE_UPLOAD = True

    blacktap_dir = os.path.dirname(sys.argv[0])
    src_dir = os.path.join(blacktap_dir, 'src')
    client_dir = os.path.join(src_dir, 'client')
    db_dir = os.path.join(src_dir, 'db')

    parser = argparse.ArgumentParser()
    # -gui USE_GUI -fs USE_FILESTREAM -u USE_UPLOAD
    parser.add_argument('-gui', '--use_gui', help="USE_GUI [bool]")
    parser.add_argument(
        '-fs',
        '--use_filestream',
        help="USE_FILESTREAM [bool]")
    parser.add_argument('-u', '--use_upload', help="USE_UPLOAD [bool]")
    args = parser.parse_args()
    if args.use_gui is not None:
        USE_GUI = args.use_gui in ('1', 'True', 'true')
    if args.use_filestream is not None:
        USE_FILESTREAM = args.use_filestream in ('1', 'True', 'true')
    if args.use_upload is not None:
        USE_UPLOAD = args.use_upload in ('1', 'True', 'true')

    devnull = subprocess.DEVNULL
    if USE_FILESTREAM:
        subprocess.Popen(
            ['nohup', 'python3', os.path.join(client_dir, 'filestream.py')])
    time.sleep(1)
    if USE_UPLOAD:
        subprocess.Popen(
            ['nohup', 'python2', os.path.join(db_dir, 'Runner.py')])

    time.sleep(1)
    subprocess.Popen(['nohup',
                      'python3',
                      os.path.join(client_dir,
                                   'main.py'),
                      '-gui',
                      str(USE_GUI),
                      '-fs',
                      str(USE_FILESTREAM),
                      '-u',
                      str(USE_UPLOAD)])


if __name__ == '__main__':
    main()
