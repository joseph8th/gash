#!/bin/bash

cur_dir=$PWD
project_dir=$1
[[ ! -e "$project_dir" ]] && echo "Directory not found: $project_dir" && exit 1
cd "$project_dir"

branch_name="$(git symbolic-ref HEAD 2>/dev/null)" ||
branch_name="(unnamed branch)"     # detached HEAD
branch_name=${branch_name##refs/heads/}
echo $branch_name

cd "$cur_dir"
