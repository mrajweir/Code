import random

POP_SIZE = 300
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.01
GENESET = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
target = input("Enter in a string and I'll try guess it - alphabetical characters and spaces only > ")
RAND_NUM = random.random()


def generate_base_population():
    population = dict()

    for _ in range(POP_SIZE):
        gene = generate_parent(len(target))
        population[gene] = 0

    return population


def extract_from_population(population):
    best = random.choice(list(population.keys()))

    for _ in range(4):
        gene = random.choice(list(population.keys()))
        if population[gene] > population[best]:
            best = gene

    return best


def generate_new_population(population):
    new_population = dict()

    while len(new_population) <= POP_SIZE:
        child_one = extract_from_population(population)
        child_two = extract_from_population(population)

        child_one, child_two = crossover(child_one, child_two)
        child_one = mutate(child_one)
        child_two = mutate(child_two)

        new_population[child_one] = 0
        new_population[child_two] = 0

    return new_population


def assign_fitness(population):
    for x in population:
        population[x] = get_fitness(x)


def generate_parent(length):
    genes = list("")
    for i in range(0, length):
        random_gene = random.choice(GENESET)
        genes.append(random_gene)
    return ''.join(genes)


def get_fitness(candidate):
    fitness = 0
    for i in range(0, len(candidate) - 1):
        if target[i] == candidate[i]:
            fitness += 1
    return fitness


def mutate(parent):
    if random.random() < MUTATION_RATE:
        gene_index_to_mutate = random.randint(0, len(parent) - 1)
        mutation_value = random.choice(GENESET)
        genes = list(parent)
        genes[gene_index_to_mutate] = mutation_value
        return ''.join(genes)

    return parent


def crossover(parent_a, parent_b):
    if random.random() < CROSSOVER_RATE:
        random_index = random.randint(0, len(target))
        parent_a_slice = parent_a[:random_index]
        parent_b_slice = parent_b[random_index:]

        return (parent_a_slice + parent_b_slice), (parent_b_slice + parent_a_slice)

    return parent_a, parent_b


def choose_child(population):
    fitness_sum = sum(population.values())
    pick = random.uniform(0, fitness_sum)
    current = 0
    for pop in population:
        current += population[pop]
        if current >= pick:
            return pop


def main():
    population = generate_base_population()

    target_not_found = True

    count = 0
    while target_not_found:
        count += 1
        print("Count [ {:04d} ] ".format(count), end='')
        print(population)

        assign_fitness(population)

        if target in population:
            print("target found!")
            target_not_found = False

        if target_not_found:
            temp_population = generate_new_population(population)
            population.clear()
            population = temp_population


main()
