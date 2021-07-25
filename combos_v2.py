# This Makes me want to vomit

def new_combos(filename, complist, adjs, result_file):
    with open(result_file, "w") as writecombos:
        with open(filename, "r") as readnames:
            # Name List
            for i in readnames:
                # Computer Terms
                with open(complist, "r") as readcomp:
                    for j in readcomp:
                        # Adjective List
                        with open(adjs, "r") as readadjs:
                            for k in readadjs:
                                for num in range (0, 100):
                                    if num == 0:
                                        # Computer Term
                                        writecombos.write(j.strip('\n') + '\n')
                                        writecombos.write(j.strip('\n') + '0' + '\n')
                                        writecombos.write(j.strip('\n') + '0' + str(num) + '\n')
                                        # Adjective
                                        writecombos.write(k.strip('\n') + '\n')
                                        writecombos.write(k.strip('\n') + '0' + '\n')
                                        writecombos.write(k.strip('\n') + '0' + str(num) + '\n')
                                        # First Name
                                        writecombos.write(i.strip('\n') + '\n')
                                        writecombos.write(i.strip('\n') + '0' + '\n')
                                        writecombos.write(i.strip('\n') + '0' + str(num) + '\n')
                                        # First Name + Computer Term
                                        writecombos.write(i.strip('\n') + j.strip('\n') + '\n')
                                        writecombos.write(i.strip('\n') + j.strip('\n') + '0' + '\n')
                                        writecombos.write(i.strip('\n') + j.strip('\n') + '0' + str(num) + '\n')
                                        # Computer Term + First Name
                                        writecombos.write(j.strip('\n') + i.strip('\n') + '\n')
                                        writecombos.write(j.strip('\n') + i.strip('\n') + '0' + '\n')                                
                                        writecombos.write(j.strip('\n') + i.strip('\n') + '0' + str(num) + '\n')
                                        # Computer Term + Adjective
                                        writecombos.write(j.strip('\n') + k.strip('\n') + '\n')
                                        writecombos.write(j.strip('\n') + k.strip('\n') + '0' + '\n')
                                        writecombos.write(j.strip('\n') + k.strip('\n') + '0'+ str(num) + '\n')
                                        # Adjective + Computer Term
                                        writecombos.write(k.strip('\n') + j.strip('\n') + '\n')
                                        writecombos.write(k.strip('\n') + j.strip('\n') + '0' + '\n')
                                        writecombos.write(k.strip('\n') + j.strip('\n') + '0' + str(num) + '\n')
                                    elif num < 10:
                                        # Computer Term
                                        writecombos.write(j.strip('\n') + '0' + str(num) + '\n')
                                        writecombos.write(j.strip('\n') + str(num) + '\n')
                                        # Adjective
                                        writecombos.write(k.strip('\n') + '0' + str(num) + '\n')
                                        writecombos.write(k.strip('\n') + str(num) + '\n')
                                        # First Name
                                        writecombos.write(i.strip('\n') + '0' + str(num) + '\n')
                                        writecombos.write(i.strip('\n') + str(num) + '\n')
                                        # First Name + Computer Term
                                        writecombos.write(i.strip('\n') + j.strip('\n') + '0' + str(num) + '\n')
                                        writecombos.write(i.strip('\n') + j.strip('\n') + str(num) + '\n')
                                        # Computer Term + First Name
                                        writecombos.write(j.strip('\n') + i.strip('\n') + '0' + str(num) + '\n')
                                        writecombos.write(j.strip('\n') + i.strip('\n') + str(num) + '\n')
                                        # Adjective + Computer Term
                                        writecombos.write(k.strip('\n') + j.strip('\n') + '0' + str(num)+ '\n')
                                        writecombos.write(k.strip('\n') + j.strip('\n') + str(num) + '\n')
                                        # Computer Term + Adjective
                                        writecombos.write(j.strip('\n') + k.strip('\n') + '0' + str(num) + '\n')
                                        writecombos.write(j.strip('\n') + k.strip('\n') + str(num) + '\n')
                                    else:
                                        # Computer Term
                                        writecombos.write(j.strip('\n') + str(num) + '\n')  
                                        # Adjective
                                        writecombos.write(k.strip('\n') + str(num) + '\n')
                                        # First Name
                                        writecombos.write(i.strip('\n') + str(num) + '\n')
                                        # First Name + Computer Term
                                        writecombos.write(i.strip('\n') + j.strip('\n') + str(num) + '\n')
                                        # Computer Term + First Name
                                        writecombos.write(j.strip('\n') + i.strip('\n') + str(num) + '\n')
                                        # Adjective + Computer Term
                                        writecombos.write(k.strip('\n') + j.strip('\n') + str(num) + '\n')
                                        # Computer Term + Adjective
                                        writecombos.write(j.strip('\n') + k.strip('\n') + str(num) + '\n')