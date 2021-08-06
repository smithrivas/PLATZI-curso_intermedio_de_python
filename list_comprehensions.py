def run():
    # Manera tradicional
    
    # squeares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squeares.append(i**2)

    
    # Manera List comprehensions

    # squeares = [i for i in range(1, 100000) if i%4==0 and i%6==0 and i%9==0]
    # squeares = [i for i in range(1, 100000) if i%36 == 0]
    print([i for i in range(1, 100000) if i%36 == 0])

if __name__ == '__main__':
    run()