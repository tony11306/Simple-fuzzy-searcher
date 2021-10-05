from ctypes import Structure, cdll, c_char_p, c_longlong

class _GoString(Structure):
    _fields_ = [
        ('p', c_char_p),
        ('n', c_longlong)
    ]


class BKTree:

    _edit_distance_lib = cdll.LoadLibrary("./dlls/editDistance.dll")

    class Node:
        def __init__(self, word: str) -> None:
            self.word: str = word
            self.children: dict[int, self] = {}
        def __str__(self) -> str:
            return self.word

    def __init__(self, tolerance=4, is_case_sensitive=True) -> None:
        self._root = None
        self._tolerance = tolerance
        self._is_case_sensitive = is_case_sensitive
        self.size = 0
    
    @staticmethod
    def _levenshtein_distance(s1: str, s2: str):

        s1_go_string = _GoString(s1.encode('utf-8'), len(s1.encode('utf-8')))
        s2_go_string = _GoString(s2.encode('utf-8'), len(s2.encode('utf-8')))
        return BKTree._edit_distance_lib.LevenshteinDistance(s1_go_string, s2_go_string)

    
    def insert(self, word: str):

        if not self._is_case_sensitive:
            word = word.lower()

        if self._root is None:
            self._root = self.Node(word)
            self.size += 1
            return
        
        current_node = self._root
        distance = self._levenshtein_distance(word, current_node.word)

        while distance in current_node.children:
            current_node = current_node.children[distance]
        
        current_node.children[distance] = self.Node(word)
        self.size += 1
    
    def find(self, key_word: str):

        if not self._is_case_sensitive:
            key_word = key_word.lower()

        if self._root is None or len(key_word) == 0:
            return []

        bfs_queue = [self._root]
        result = []

        while len(bfs_queue) > 0: # while queue is not empty
            distance = self._levenshtein_distance(bfs_queue[0].word, key_word)
            if distance <= self._tolerance:
                result.append(bfs_queue[0].word)
            
            for key, value in bfs_queue[0].children.items():
                if key >= distance - self._tolerance and key <= distance + self._tolerance:
                    bfs_queue.append(value)
            
            bfs_queue.pop(0)
            
        return result
    
    def find_best(self, word: str):
        if not self._is_case_sensitive:
            word = word.lower()

        result = self.find(word)

        if len(result) == 0:
            return ""
        result = sorted(
            result, 
            key=lambda x: (
                -BKTree._edit_distance_lib.LongestCommonSubsequenceLength(_GoString(word.encode('utf8'), len(word.encode('utf8'))), _GoString(x.encode('utf8'), len(x.encode('utf8')))),
                abs(len(word)-len(x)),
            )
        )
        return result[0]

