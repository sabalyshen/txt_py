import os
import shutil  

for file in os.listdir('data'): 
    f = open(os.path.join('data', file), 'r+', encoding = 'utf8')
    f2 = open(os.path.join('output','output' + file), 'w+', encoding = 'utf8')
    for line in f.readlines():
        line = line.replace('\n', '')
        if '(1)' or '(2)' in line:
            line = line.split(' ')
            w_list = [line[0]]
            for w in line:
                if '(1)' in w:
                    w_list.append(w)
                elif '(2)' in w:
                    w_list.append(w)
                    w_list.reverse() 
            if w_list == [''] or None:
                pass  
            else:
                try:
                    w_list.append('\n')
                    w_list2 = []
                    for l in w_list:
                        w_list2.append(l.replace('(1)', '').replace('(2)', '').replace('_', ' ') + ' ')
                    f2.writelines(w_list2)
                except:
                    pass
        else:
            line = line.replace('_', ' ')
            f2.write(line + '\n')
    f.close
    f2.close

       

