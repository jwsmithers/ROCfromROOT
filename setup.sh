# This is needed to get the proper Python stuff in order to run
echo
echo "======================INFO:=========================="
echo "Setting up the environment to create ROC curves "
echo "====================================================="
echo

lxplus="$( env | grep lxplus)"

if [[ "$lxplus" != "" ]] ; then
  echo -n "INFO: Start setupATLAS..."
  setupATLAS 1>/dev/null
  echo "done"

  echo -n "INFO: lsetup \"lcgenv\"..."
  lsetup "lcgenv -p LCG_86 x86_64-slc6-gcc49-opt pip" 1>/dev/null
  lsetup "lcgenv -p LCG_86 x86_64-slc6-gcc49-opt root_numpy" 1>/dev/null
  lsetup "lcgenv -p LCG_86 x86_64-slc6-gcc49-opt rootpy" 1>/dev/null
  echo "done"

  echo -n "INFO: load required python modules..."
  pip install --user numpy 1>/dev/null 2>/dev/null
  pip install --user joblib 1>/dev/null 2>/dev/null
  pip install --user sklearn 1>/dev/null 2>/dev/null
  echo "done"
fi
