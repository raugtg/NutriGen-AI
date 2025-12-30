{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7633b798-a116-4570-be43-c5184918ee5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "def filter_makanan_manusia_normal_final(df):\n",
    "    menu_umum = ['nasi', 'mie', 'ayam', 'ikan', 'telur', 'daging', 'sapi', 'tempe', 'tahu', 'sayur', 'sop', 'soto', 'pisang', 'pepaya', 'jeruk', 'roti', 'kentang', 'tuna', 'udang']\n",
    "    \n",
    "    kata_haram = [\n",
    "        'ampas', 'biji', 'kulit', 'darah', 'mentah', 'tepung', 'minyak', 'lemak', \n",
    "        'bubuk', 'buah merah', 'biang', 'ekstrak', 'asam', 'ragi', 'mentega', \n",
    "        'ginjal', 'ndusuk', 'nipis', 'ledre', 'kecimpring', 'putu', 'kepok',\n",
    "        'penyu', 'maleo', 'hutan', 'kucing', 'anjing', 'hiu'\n",
    "    ]\n",
    "    \n",
    "    pattern_menu = '|'.join(menu_umum)\n",
    "    pattern_haram = '|'.join(kata_haram)\n",
    "    \n",
    "    df_clean = df[df['Nama'].str.contains(pattern_menu, case=False, na=False)].copy()\n",
    "    df_clean = df_clean[~df_clean['Nama'].str.contains(pattern_haram, case=False, na=False)]\n",
    "    \n",
    "    is_mentah = (df_clean['Nama'].str.contains('segar', case=False)) & \\\n",
    "                (df_clean['Nama'].str.contains('ikan|ayam|daging|sapi|telur', case=False))\n",
    "    \n",
    "    return df_clean[~is_mentah]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "adbcfb62-04f4-4d33-ad87-b3f0e185d6fa",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
