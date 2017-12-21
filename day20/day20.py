import re
import itertools

class particle:
    p = []
    v = []
    a = []
    num = -1
    destroyed = False


def process_collisions(particles):
    # updates the destroyed property of each particle

    for pair in itertools.combinations(particles, 2):
        if pair[0].p == pair[1].p:
            particles[pair[0].num].destroyed = True
            particles[pair[1].num].destroyed = True





def count_particles_remaining(particles):
    count = 0
    for particle in particles:
        if particle.destroyed is False:
            count += 1
    return count


def update_particles_p_v(particles):
    for i in range(len(particles)):
        particles[i].v[0] += particles[i].a[0]
        particles[i].v[1] += particles[i].a[1]
        particles[i].v[2] += particles[i].a[2]

        particles[i].p[0] += particles[i].v[0]
        particles[i].p[1] += particles[i].v[1]
        particles[i].p[2] += particles[i].v[2]

    return particles



    return particles

def step(particles):
    # returns updated set of particles
    particles = update_particles_p_v(particles)
    process_collisions(particles)

    particles_remaining = count_particles_remaining(particles)
    print(f"Particles remaining: {particles_remaining}")
    return particles



def particle_from_line(line, i):
    new_particle = particle()

    components = line.split('>')
    p_string = components[0]
    v_string = components[1]
    a_string = components[2]

    m = re.search("(?<=p=<).+", p_string)
    pxyz = m.group(0).split(',')
    m = re.search("(?<=v=<).+", v_string)
    vxyz = m.group(0).split(',')
    m = re.search("(?<=a=<).+", a_string)
    axyz = m.group(0).split(',')

    px = int(pxyz[0])
    py = int(pxyz[1])
    pz = int(pxyz[2])

    vx = int(vxyz[0])
    vy = int(vxyz[1])
    vz = int(vxyz[2])

    ax = int(axyz[0])
    ay = int(axyz[1])
    az = int(axyz[2])

    new_particle.p = [px, py, pz]
    new_particle.v = [vx, vy, vz]
    new_particle.a = [ax, ay, az]
    new_particle.num = i

    return new_particle



if __name__ == "__main__":
    particles = [particle_from_line(line, i) for i, line in enumerate(open("input.txt", "r").readlines())]

    # find the minimum absolute manhattan acceleration
    min_a = 9999999
    min_i = -1
    for i, p in enumerate(particles):
        a = p.a
        abs_a_manhattan = abs(a[0]) + abs(a[1]) + abs(a[2])
        if abs_a_manhattan < min_a:
            min_a = abs_a_manhattan
            min_i = i

    print(f"Part 1: Particle # {min_i}")


    for i in range(50):
        particles = step(particles)
