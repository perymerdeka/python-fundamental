data_diri = {
    'identitas': [
        {'nama': 'Feri', 'Negara': 'Indonesia'},
        {'nama': 'Dwipangga', 'Negara': 'Singapura'},
        {'nama': 'Salman', 'Negara': 'Malaysia'}
    ]
}

for data in data_diri['identitas']:
    print('Data nama', data['nama'])
    print('=' * 10)
    print('Data Asal Negara', data['Negara'])

print('Total data Imigran: ', len(data_diri['identitas']))