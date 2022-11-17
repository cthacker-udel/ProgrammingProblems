from random import randint

# Constant values to be used for the scoring grid in the Needleman-Wunsch algorithm
IDENTITY = 4
TRANSITION = -2
TRANSVERSION = -3
GAP = -8
SCORES = { # scoring matrix for the Needleman-Wunsch algorithm
    "A" : {
        "A" : IDENTITY,
        "T" : TRANSVERSION,
        "C" : TRANSVERSION,
        "G" : TRANSITION
    },
    "T" : {
        "A" : TRANSVERSION,
        "T" : IDENTITY,
        "C" : TRANSITION,
        "G" : TRANSVERSION
    },
    "C" : {
        "A" : TRANSVERSION,
        "T" : TRANSITION,
        "C" : IDENTITY,
        "G" : TRANSVERSION
    },
    "G" : {
        "A" : TRANSITION,
        "T" : TRANSVERSION,
        "C" : TRANSVERSION,
        "G" : IDENTITY
    }
}

# left, up, diagonal, used to fill direction matrix path for backpropagation
DIRECTIONS = ("DIAG", "LEFT", "UP")

def get_seq() -> tuple[str, str]:
    """Prompt user for sequences to be used in the Needleman-Wunsch algorithm,
    then read and format sequences.

    Returns a tuple of cleaned DNA sequence strings.
    """
    seq = ["", ""]
    path = input("Please enter a filepath containing two sequences:\n").strip()

    try:
        with open(path, "r", encoding='utf-8') as f:
            lines = f.readlines()
            idx_1, idx_2 = None, None
            for i in range(len(lines)):
                if lines[i].startswith(">"):
                    if idx_1 == None:
                        idx_1 = i
                    elif idx_2 == None:
                        idx_2 = i
                        break
            
            # Format txt file input of FASTA seq into a continuous string of nucleotides
            try:
                seq[0] = "".join(lines[idx_1+1:idx_2]).upper().replace("\n", "")
                seq[1] = "".join(lines[idx_2+1:]).upper().replace("\n", "")
            except TypeError as e:
                print(e, "\nFile must be in the form of\n>SEQUENCE 1 NAME\nAGTC ... GTA\n>SEQUENCE 2 NAME\nTGAT ... CCA")
    except FileNotFoundError as e:
        print("ERROR READING FILEPATH: ", e)

    
    return seq

def make_matrix(seq_1:str, seq_2:str, make_dir:bool) -> list[list]:
    """Create grid of values to be used for the Needleman-Wunsch algorithm
    This matrix is in the form of:
    [
        [_, _, A, T, A, ..., G]
        [_, 0, _, _, _, ..., _]
        ...
        [A, _, _, _, _, ..., _]
    ]

    if make_dir is True, the [1][1] position contains the string 'DONE' to halt
    back propagation, and the first row/col axes have 'LEFT' and 'UP' directions,
    respectively

    otherwise, fill the valued matrix alongside the first row/col by multiples
    of the GAP penalty
    """

    # initialize empty array
    mat = [ [None]*(len(seq_2) + 2) for i in range(len(seq_1) + 2) ]

    if make_dir: # fill direction matrix
        # make seq 1 exist along the y axis (rows)
        for i in range(len(seq_1)):
            mat[i+2][0] = seq_1[i]
            mat[i+2][1] = DIRECTIONS[0]

        # make seq 2 exist along the x axis (cols)
        for i in range(len(seq_2)):
            mat[0][i+2] = seq_2[i]
            mat[1][i+2] = DIRECTIONS[1]
    else: # fill value matrix
        # make seq 1 exist along the y axis (rows)
        for i in range(len(seq_1)):
            mat[i+2][0] = seq_1[i]
            mat[i+2][1] = GAP*(i+1)

        # make seq 2 exist along the x axis (cols)
        for i in range(len(seq_2)):
            mat[0][i+2] = seq_2[i]
            mat[1][i+2] = GAP*(i+1)

    mat[1][1] = "DONE" if make_dir else 0
    
    return mat

def fill_matrix(mat:list[list], mat_dir:list[list], x:int, y:int, max_x:int, max_y:int) -> None:
    """Uses the scores matrix to fill values and directions for the Needleman-Wunsch algorithm grid"""
    # end if x or y positions are out of bounds or mat not initialized
    if mat == None or x > max_x or y > max_y:
        return
    # end if None is at the current position, the left, or above
    if mat[y][x] != None or mat[y-1][x] == None or mat[y][x-1] == None:
        return

    # find the score that corresponds to the index/column of current position
    score = SCORES[mat[y][0]] [mat[0][x]]

    # get list of the 3 possible new values
    values = [
        mat[y-1][x-1] + score, # value coming from diagonal,
        mat[y][x-1] + GAP,  # value coming from left
        mat[y-1][x] + GAP,  # value coming from up
    ]

    max_val = max(values)   # max val
    max_idx = values.index(max_val) # index corresponds to the back-propagation movement, prioritizes first index (diagonal)
    if max_idx > 0 and values[1] == values [2]:
        max_idx = randint(1,2) # if theres a tie between left and up, randomly pick one

    mat[y][x] = max_val # make position's value the best scoring outcome
    mat_dir[y][x] = DIRECTIONS[max_idx] # make positions value the backprop direction

    fill_matrix(mat, mat_dir, x+1, y, max_x, max_y)  # recusively fill values by moving right
    fill_matrix(mat, mat_dir, x, y+1, max_x, max_y)  # recursively fill values by moving down

def get_alignment(mat:list[list], mat_dir:list[list]) -> tuple[str, str, int]:
    """Uses a filled direction matrix and uses the Needleman-Wunsch algorithm to get the
    best scoring alignment via backpropogation. The maximum value is also obtained from
    the valued matrix
    
    Function returns a tuple containing an optimal alignment for seq1, seq2, and the best
    score associated with the alignment"""
    x = len(mat[0]) -1
    y = len(mat) -1
    best_score = mat[y][x]

    align_1 = ""  # vertical seq
    align_2 = ""  # horizontal seq
    while mat_dir[y][x] != "DONE":
        direction = mat_dir[y][x]

        if direction == "DIAG":
            # backpropagation must move diagonally
            align_1 = mat_dir[y][0] + align_1
            align_2 = mat_dir[0][x] + align_2
            x -= 1
            y -= 1
        elif direction == "LEFT":
            # backpropagation must move left
            align_1 = "-" + align_1
            align_2 = mat_dir[0][x] + align_2
            x -=1
        else:
            # backpropagation must move up
            align_1 = mat_dir[y][0] + align_1
            align_2 = "-" + align_2
            y -=1

    return (align_1, align_2, best_score)

def print_align_results(align_1:str, align_2:str, score:int) -> None:
    """Takes the aligned sequences strings and best score, then prints out the results"""
    print(f"SEQUENCE 1:\t{align_1}")
    print(f"SEQUENCE 2:\t{align_2}")
    print("Alignment Score:", score)

def print_mat(mat:list[list]) -> None:
    """cleanly prints a provided matrix"""
    for row in mat:
        for i in row:
            print("_" if i == None else i, end="\t")
        print("\n")

if __name__ == "__main__":
    while True:
        seq1, seq2 = get_seq()
        if seq1 == "" or seq2 == "":
            print("Inputs contain invalid sequences, please check your FASTA files.")
        else:
            mat = make_matrix(seq1, seq2, make_dir=False)
            mat_dir = make_matrix(seq1, seq2, make_dir=True)

            fill_matrix(mat, mat_dir, 2, 2, len(mat[0])-1, len(mat)-1)

            align_1, align_2, score = get_alignment(mat, mat_dir)

            print("############ DYNAMIC PROGRAMMING TABLE ############\n")
            print_mat(mat)
            print_mat(mat_dir)

            print("############ ALIGNMENT RESULTS ############\n")
            print_align_results(align_1, align_2, score)

        if input("Would you like to align sequences again? (y/n)").strip().lower() == "y":
            continue
        else:
            break