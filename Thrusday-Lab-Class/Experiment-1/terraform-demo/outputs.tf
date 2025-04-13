output "instance_id" {
  value = aws_instance.mlops_vm.id
}

output "public_ip" {
  value = aws_instance.mlops_vm.public_ip
}
