import os
import subprocess

for i in os.listdir():
    if not i.endswith('.Rmd'):
        continue
    #subprocess.call("export PATH=$PATH:/Applications/RStudio.app/Contents/MacOS/pandoc", shell=True)
    cmd = f'R -e "rmarkdown::render(\'{i}\')"'
    print(cmd)
    subprocess.call(cmd, shell=True)

    html_name = i.split('.Rmd')[0] + '.html'
    md_name = i.split('.Rmd')[0] + '.md'

    subprocess.call(f"mv {html_name} /Users/sebastian/OneDrive/project-data/admin__website-personal/website/resources/r-notes", shell=True)

os.chdir("/Users/sebastian/OneDrive/project-data/admin__website-personal/website/")
subprocess.call("jekyll build", shell=True)
print("/Users/sebastian/OneDrive/project-data/admin__website-personal/website/")
