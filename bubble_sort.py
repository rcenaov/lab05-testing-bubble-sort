class BubbleSort:
    def sort(self, vet: list[int]) -> None:
        for i in range(len(vet), 1, -1):
            for j in range(1, i):
                if vet[j - 1] > vet[j]:
                    aux = vet[j - 1]
                    vet[j - 1] = vet[j]
                    vet[j] = aux