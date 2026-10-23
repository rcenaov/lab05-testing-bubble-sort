from bubble_sort import BubbleSort

class TestBubbleSort:
    def setup_method(self):
        self.sut = BubbleSort()

    def teardown_method(self):
        self.sut = None

    def test_cp1_vacio(self):
        arr = []
        self.sut.sort(arr)
        # Assert
        assert arr == []

    def test_cp1_un_elemento(self):
        arr = [7]
        self.sut.sort(arr)
        assert arr == [7]

    def test_cp2(self):
        arr = [1, 2]
        self.sut.sort(arr)
        assert arr == [1, 2]

    def test_cp3(self):
        arr = [2, 1]
        self.sut.sort(arr)
        assert arr == [1, 2]

    def test_cp4(self):
        arr = [3, 2, 1]
        self.sut.sort(arr)
        assert arr == [1, 2, 3]