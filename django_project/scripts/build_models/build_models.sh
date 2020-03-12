#!/bin/sh
root=$HOME"/github/important-stuff/django_project"
build_dir=$root"/scripts/build_models"
final_dir=$root"/apps/models"
cd $root

echo "Running inspectdb command ..."
python3 manage.py inspectdb>models.py
if [[ $? -ne 0 ]]; then
    "Inspectdb command failed"
    exit 1
fi
echo "Created models.py file"


mv $root"/models.py" $build_dir
echo "Moved models.py to $build_dir"
cd $build_dir

echo "Running create_models_dir.py ..."
python3 create_models_dir.py models.py
if [[ $? -ne 0 ]]; then
    echo "error while running create_models_dir.py"
    exit 1
fi

echo "creating $final_dir directory"
mkdir $final_dir
prev_status=$?
confirm="yes"
if [[ $prev_status -ne 0 ]]; then
    if [[ $prev_status -eq 1 ]]; then
        echo "$final_dir dir already exists"

        read -p "delete $final_dir? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || confirm="no" 
        # echo $confirm
        if [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]; then
            echo "deleting $final_dir directory"
            rm -r $final_dir
        else
            echo "Operation aborted"
            # exit 1
        fi
    else
        echo "mkdir $final_dir Exit with status $prev_status"
    fi  
fi


if [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]; then
    echo "moving models under apps ..."
    # mv $root"/scripts/build_models/models" $root"/apps/"
    mv $build_dir"/models" $final_dir
    if [[ $? -ne 0 ]]; then
        echo "error while moving files under apps/models"
        exit 1
    fi

    echo "Files Moved successfully"
fi

rm -r $build_dir"/models.py"
if ! [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]; then
    rm -r $build_dir"/models" 
fi

cd $root