CWD="$(dirname "$0")"
LICORICE_WORKING_PATH=$CWD LICORICE_TEMPLATE_PATH="$CWD/../../../lico_drivers/drivers" licorice go synth.yaml -y  "$@"
