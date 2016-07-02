from sampleapp.worker import name as webjob_name
import os
import sys
import shutil

if __name__ == "__main__":
    try:
        wwwroot = os.environ['WEBROOT_PATH']
        src_path = os.path.join(wwwroot, 'sampleapp', 'worker', 'run.py')
        dest_dir = os.path.join(wwwroot, 'App_Data', 'jobs', 'continuous', webjob_name)
        shutil.copy(src_path, dest_dir)
    except Exception as e:
        print("failed to deploy webjob with reason: " + str(e))
        sys.stdout.flush()
