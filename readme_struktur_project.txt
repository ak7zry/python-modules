---------------------------------------------------------------------------
                             STRUKTUR PROJECT
---------------------------------------------------------------------------
## saat project python besar dan komplek perlu adanya struktur project :

^^ untuk mengorganisir kode 
^^ kode lebih mudah dipahami : programmer lain bisa cepat memahami PROJECT
^^ maintenance lebih mudah   : bux fixing dan feature baru lebih mudah
^^ reusability tinggi        : modules bisa digunakan ulang
^^ collaboration             : tim bisa kerja pada bagian berbeda
^^ testing                   : setiap bagian bisa di tes secara terpisah
---------------------------------------------------------------------------

---------------------------------------------------------------------------
                          CONTOH STRUKTUR PROJECT
---------------------------------------------------------------------------
^^ project kecil :
    ________________________________________

    my_small_project/
    main.py         #entry point
    utils.py        #helper functions
    config.py       #konfigurasi
    README.md       #dokumentasi
    ________________________________________

^^ project medium :

    ________________________________________

    my_medium_project/
    main.py                 # entry point
    config.py               # konfigurasi
    requiremnets.txt        # dependensi
    README.md               # dokumentasi
    modules/                # package modules 
        __init__.py
        database.py         # database operations
        api.py              # API functions
        utils.py            # utilities
    data/                   # folder untuk data files
        input.txt
        output.csv
    ________________________________________


^^ project besar / kompleks : 
    ________________________________________

    my_large_project/
    main.py                 
    config.py               
    requiremnets.txt        
    README.md   
    src/                            # source code utama >> biasanya berisi modules
        __init__.py
        core/                       # core functionality
            __init__.py
            engine.py
            processor.py
        utils/                      # utility modules
            __init__.py
            helpers.py
            validators.py
        models/                     # data models
            __init__.py
            user.py
            product.py                       
    data/                           # data files
        raw/
        processed/
    tests/                          # testing files
        __init__.py
        test_core.py
        test_utils.py
    docs/                           # documentation
        manual.md
    ________________________________________
