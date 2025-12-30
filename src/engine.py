{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab2048aa-3eef-4f31-8d73-98b9ef0e3213",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "from src.nutrition import apply_guardrails\n",
    "\n",
    "def hitung_fitness_bundle(menu, target):\n",
    "    total = {'Energi': 0, 'Protein': 0}\n",
    "    bahan_utama = [m['nama'].split()[0].lower() for m in menu]\n",
    "    \n",
    "    for m in menu:\n",
    "        f = m['porsi'] / 100\n",
    "        total['Energi'] += m['energi'] * f\n",
    "        total['Protein'] += m['protein'] * f\n",
    "\n",
    "    # Logic Diversity Penalty yang kita buat\n",
    "    pinalti_duplikat = 0\n",
    "    jumlah_unik = len(set(bahan_utama))\n",
    "    if jumlah_unik < len(bahan_utama):\n",
    "        pinalti_duplikat = (len(bahan_utama) - jumlah_unik) * 2000\n",
    "\n",
    "    diff_e = abs(total['Energi'] - target['Energi'])\n",
    "    if total['Energi'] > target['Energi']: diff_e *= 50\n",
    "    \n",
    "    diff_p = total['Protein'] - target['Protein']\n",
    "    pinalti_p = abs(diff_p) * 100 if diff_p < 0 else abs(diff_p) * 5\n",
    "\n",
    "    error = diff_e + pinalti_p + pinalti_duplikat\n",
    "    return 1 / (1 + error), total\n",
    "\n",
    "def run_genetic_algorithm(db, target, populasi=100, generasi=100):\n",
    "    # Masukkan loop utama GA lo di sini (Selection, Crossover, Mutation)\n",
    "    pass"
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
