hordo = int(input('hány literes a hordó? '))
kancso = int(input('hány literes a kancsó? '))

print(f'A hordóból összesen {hordo // kancso} db teli kancsó mérhető ki')
print(f'Ha kimerünk ennyi kancsó vizet, {hordo % kancso} liter víz marad.')
print(f'A hordó és kancsó térfogatának hányadosa: {round(hordo / kancso, 3)}')