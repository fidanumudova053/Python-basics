kofe = 4.5
cizkeyk = 6.0
su = 1.0

# Hesablamalar
cemi = kofe + cizkeyk + su
edv = cemi * 0.18
yekun = cemi + edv

# Çek formasında ekrana çıxarılması
print("------ KAFE ------")
print(f"Kofe     {kofe} AZN")
print(f"Çizkeyk  {cizkeyk} AZN")
print(f"Su       {su} AZN")
print("------------------")
print(f"Cəmi:    {cemi} AZN")
print(f"ƏDV 18%: {edv:.2f} AZN")
print(f"Yekun:   {yekun:.2f} AZN")
