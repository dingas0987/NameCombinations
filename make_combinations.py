# FIND MORE ADJECTIVES/HIGHER QUALITY ADJECTIVES

def make_combo(filename, adj):
    with open('name_combinations_comp_term.txt', 'w') as combos:
        with open(filename, 'r') as readname:
            for i in readname:
                with open(adj, 'r') as readadj:
                    for j in readadj:
                        for num in range(0, 100):
                            if num == 0:
                                combos.write(i.strip('\n') + j.strip('\n') + '\n')
                                combos.write(j.strip('\n') + i.strip('\n') + '\n')
                                combos.write(i.strip('\n') + j.strip('\n') + '0' + '\n')
                                combos.write(j.strip('\n') + i.strip('\n') + '0' + '\n')                                
                                combos.write(i.strip('\n') + j.strip('\n') + '0' + str(num) + '\n')
                                combos.write(j.strip('\n') + i.strip('\n') + '0' + str(num) + '\n')
                            elif num < 10:
                                combos.write(i.strip('\n') + j.strip('\n') + '0' + str(num) + '\n')
                                combos.write(j.strip('\n') + i.strip('\n') + '0' + str(num) + '\n')
                                combos.write(i.strip('\n') + j.strip('\n') + str(num) + '\n')
                                combos.write(j.strip('\n') + i.strip('\n') + str(num) + '\n')
                            else:
                                combos.write(i.strip('\n') + j.strip('\n') + str(num) + '\n')
                                combos.write(j.strip('\n') + i.strip('\n') + str(num) + '\n')                       

#if __name__ == '__main__':
#    name_list = 'male.txt'
#    adj_list = 'adjectives.txt'
#    make_combo(name_list, adj_list)