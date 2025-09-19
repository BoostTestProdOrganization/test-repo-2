# app/controllers/users_controller.rb
# This file contains various SQL injection vulnerabilities for testing Brakeman

class UsersController < ApplicationController
  
  # SQL Injection - Direct interpolation (High severity)
  def vulnerable_find_by_name
    name = params[:name]
    User.where("name = '#{name}'")  # Brakeman will flag this
  end
  
  # SQL Injection - Using find_by_sql (High severity)
  def vulnerable_find_by_sql
    id = params[:id]
    User.find_by_sql("SELECT * FROM users WHERE id = #{id}")  # Vulnerable
  end
  
  # SQL Injection - Dynamic ORDER BY (Medium severity)
  def vulnerable_order_by
    sort_column = params[:sort]
    User.order("#{sort_column} ASC")  # Vulnerable to column injection
  end
  
  # SQL Injection - LIKE query (High severity)
  def vulnerable_search
    search_term = params[:q]
    User.where("name LIKE '%#{search_term}%'")  # Vulnerable
  end
  
  # SQL Injection - Multiple parameters (High severity)
  def vulnerable_complex_query
    status = params[:status]
    role = params[:role]
    User.where("status = '#{status}' AND role = '#{role}'")  # Vulnerable
  end
  
  # SQL Injection - IN clause (High severity)
  def vulnerable_in_clause
    ids = params[:ids]
    User.where("id IN (#{ids})")  # Vulnerable
  end
  
  # Safe version for comparison
  def safe_find_by_name
    name = params[:name]
    User.where(name: name)  # Safe - uses parameterized query
  end

end
