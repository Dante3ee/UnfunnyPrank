import os
import sys
import subprocess
import importlib.util

package_spec = importlib.util.find_spec("pycaw")
package_installed_before = package_spec is not None  #if installed before -> won't uninstall later

subprocess.check_call([sys.executable, "-m", "pip", "install", "pycaw"])

from pycaw.pycaw import AudioUtilities

sessions = AudioUtilities.GetAllSessions()        
for session in sessions:
    volume = session.SimpleAudioVolume                    
    if volume.GetMute() == 0:
        volume.SetMute(1, None) 
    else:
        volume.SetMute(0, None)

#creating the cure
remedy = f"""
import os
import sys
import subprocess
import importlib.util
from pycaw.pycaw import AudioUtilities

sessions = AudioUtilities.GetAllSessions()        
for session in sessions:
    volume = session.SimpleAudioVolume                    
    if volume.GetMute() == 0:
        volume.SetMute(1, None) 
    else:
        volume.SetMute(0, None)

for f in ["README.md", "LICENSE"]:   #vanish from disk
    if os.path.exists(f):
        os.remove(f)
"""

if not package_installed_before:
    remedy += """\nsubprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", "pycaw"])"""

with open("remedy.py", "w") as f:
    f.write(remedy)
    f.write("\nos.remove(__file__)")

os.remove(__file__) #Goodbye cruel world or is it world saying goodbye to me?
