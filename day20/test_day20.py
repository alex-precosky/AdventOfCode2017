from day20 import particle_from_line

def test_particle_from_line_a():
    line = "p=<-391,1353,-387>, v=<-94,-42,0>, a=<14,-5,3>"

    my_particle = particle_from_line(line)

    print(my_particle.a)

    assert my_particle.a == [14, -5, 3]
