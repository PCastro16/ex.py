class Imprimir:
    def desenharNaTela(self, nErros):
        self.nErros = nErros

        if self.nErros == 0:
            print("""
              |||||||||||||
              ++
              ++
              ++
              ++
              ++
              ++
              ++
              ++
              ++
              ++
              ++
              ++
             ++++
            ++++++
            """)

        elif self.nErros == 1:
            print("""
              |||||||||||||
              ++         ***
              ++        *   *
              ++         ***
              ++
              ++
              ++
              ++
              ++
              ++
              ++
              ++
              ++
             ++++
            ++++++
            """)

        elif self.nErros == 2:
            print("""
              |||||||||||||
              ++         ***
              ++        *   *
              ++         ***
              ++          |
              ++          |
              ++          |
              ++          |
              ++
              ++
              ++
              ++
              ++
             ++++
            ++++++
            """)

        elif self.nErros == 3:
            print("""
              |||||||||||||
              ++         ***
              ++        *   *
              ++         ***
              ++         /|
              ++        / |
              ++          |
              ++          |
              ++
              ++
              ++
              ++
              ++
             ++++
            ++++++
            """)

        elif self.nErros == 4:
            print("""
              |||||||||||||
              ++         ***
              ++        *   *
              ++         ***
              ++         /|\ 
              ++        / | \ 
              ++          |
              ++          |
              ++
              ++
              ++
              ++
              ++
             ++++
            ++++++
            """)

        elif self.nErros == 5:
            print("""
              |||||||||||||
              ++         ***
              ++        *   *
              ++         ***
              ++         /|\ 
              ++        / | \ 
              ++          |
              ++          |
              ++         /
              ++        /
              ++
              ++
              ++
             ++++
            ++++++
            """)

        else:
            print("""
              |||||||||||||
              ++         ***
              ++        *   *
              ++         ***
              ++         /|\ 
              ++        / | \ 
              ++          |
              ++          |
              ++         / \ 
              ++        /   \ 
              ++
              ++
              ++
             ++++
            ++++++
            """)