from make_combinations import *
from combine_files import *
from unique_text_writer import *
from combos_v2 import *
from combine_names import *

if __name__ == '__main__':
    input_files = ['adjectives.txt', 'english-adjectives.txt'] 
    output = 'res_adj.txt'

    combine_files(input_files, 'combined_adj.txt')
    dupe_search_set('combined_adj.txt', output)

    # Original Name + Adjective + Number Combo
    #make_combo('male.txt', output)

    # Updated Combo with inclusion of computer terms
    new_combos('male_test.txt', 'computer_programming_terms.txt', output, 'updated_combos.txt')

    # TESTING STUFF
    #input_files = ['male_test.txt', 'adj_list_test.txt', 'comp_term_test.txt']
    #output = 'res_test.txt'

    #combine_files(input_files, 'combined_test.txt')
    #dupe_search_set()
    #new_combos('male_test.txt', 'adj_list_test.txt', 'comp_term_test.txt', 'result_test_updated.txt')