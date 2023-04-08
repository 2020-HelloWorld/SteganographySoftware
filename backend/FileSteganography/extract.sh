content=$(cat temp.dat)
echo "${content#*C37DA957D83D607956789910AA4096C43734A220}" > "$1"