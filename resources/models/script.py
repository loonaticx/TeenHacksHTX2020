import os
os.chdir('./misc')
for file in os.listdir('.'):
    if file.endswith('.pz'):
        os.system('punzip {0}'.format(file))

for file in os.listdir('.'):
    if file.endswith('.egg'):
        os.system('egg2bam -o {0} {1}'.format(file.replace('.egg', '.bam'), file))
        os.remove(file)