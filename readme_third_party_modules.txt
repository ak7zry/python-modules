-------------------------------------------------------------------
                    THIRD PARTY PACKAGES
-------------------------------------------------------------------
^^ modules yang dibuat komunitas python dan bebas digunakan siapa saja
^^ seperti toko aplikasi python - ada ribuan packages yang bisa membantu membuat program lebih cepat
-------------------------------------------------------------------

-------------------------------------------------------------------
                 PyPI - PYTHON PACKAGE INDEX
-------------------------------------------------------------------
^^ PyPI : reposirtori resmi untuk python packages > 600.000 packages gratis
^^ https:/pypi.org
^^ contoh :
    ## untuk web >> FastAPI
-------------------------------------------------------------------

-------------------------------------------------------------------
                 Pip - Package Manager Python
-------------------------------------------------------------------
^^ pip : tootl untuk menginstall dan mengelola python packages
^^ pip sudah terinstall otomatus saat install python
^^ perintah dasar :
    >> install package               : pip install nama_package
    >> install versi tertentu        : pip install nama_package==1.2.3
    >> upgrade package               : pip install --upgrade nama_package
    >> uninstall package             : pip uninstall nama_package
    >> lihat package yang terinstall : pip list
    >> lihat info package            : pip show nama_package
    >> install dari requirements.txt : pip install -r requirements.txt
-------------------------------------------------------------------

-------------------------------------------------------------------
                        VIRTUAL ENVIRONMENT
-------------------------------------------------------------------
^^ virtual environment : memisahkan dependensi (package yang digunakan) antar project
^^ setiap project bisa punya package berbeda tanpa konflik
^^ cara buat virtual environment :
    >> buat virtual environment, biasanya nama folder .venv / .env
        python -m venv nama_folder

    >> aktifkan (windows)
        my_project_env\Scripts\activate

    >> aktifkan (mac/linux)
        source my_project_env/bin/activate
        
    >> install packages dalam environment
        pip install request colorama
    >> deaktif
        deactivate

^^ keuntungan :
    >> isolasi dependensi   : setiap project terpisah
    >> versi packages berbeda untuk project yang berbeda
    >> clean installation   : tidak mencemari sistem python
    >> easy development     : mudah replicate environment
-------------------------------------------------------------------

-------------------------------------------------------------------
                        REQUIREMENTS.TXT
-------------------------------------------------------------------
^^ berisi daftar packages yang dibutuhkan project
^^ memudahkan sharing project dan setup environment
^^ untuk membuat file dari package yang sudah terinstall :
    >> pip freeze >> requirements.txt
^^ cara install dari file requirements.txt :
    >> pip install -r requirements.txt
-------------------------------------------------------------------