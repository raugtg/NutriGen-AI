{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49a9717f-869b-480a-b66c-507aa912a458",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "def hitung_tdee(berat, tinggi, usia, gender, level_aktivitas, langkah, durasi_olahraga):\n",
    "    # Masukkan logika rumus TDEE lo di sini\n",
    "    # Jangan lupa tambahkan logic Goal (naik/turun/tetap)\n",
    "    pass\n",
    "\n",
    "def apply_guardrails(porsi, kategori, nama):\n",
    "    # Logika porsi 50-200 gram yang lo buat tadi\n",
    "    if kategori == 'karbo':\n",
    "        return min(max(porsi, 100), 200)\n",
    "    return min(max(porsi, 50), 150)"
   ]
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
