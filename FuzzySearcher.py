from BKTree import BKTree

class FuzzySearcher:

    _dictionary: list[str] = None
    _bktree: BKTree = None

    def __init__(self, is_case_sensitive=True, tolerance=2) -> None:
        if FuzzySearcher._dictionary is None:
            self._load_dictionary()
        if FuzzySearcher._bktree is None:
            self._load_bktree(is_case_sensitive, tolerance)

    @staticmethod
    def _load_dictionary():
        FuzzySearcher._dictionary = []
        with open('dictionary.txt', 'r') as f:
            line = f.readline()
            line = line.strip('\n')
            while line:
                FuzzySearcher._dictionary.append(line)
                line = f.readline()
                line = line.strip('\n')
    
    @staticmethod
    def _load_bktree(is_case_sensitive, tolerance):
        FuzzySearcher._bktree = BKTree(is_case_sensitive=is_case_sensitive, tolerance=tolerance)
        for word in FuzzySearcher._dictionary:
            FuzzySearcher._bktree.insert(word)

    def get_best_match(self, word: str) -> str:
        return self._bktree.find_best(word)
    
    def get_possible_matches(self, word: str):
        return self._bktree.find(word)
