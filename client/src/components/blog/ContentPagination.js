import React from "react";

const ContentPagination = () => {
  return (
    <div class="col-lg-12 col-md-12">
      <div class="pagination-area">
        <nav aria-label="Page navigation example">
          <ul class="pagination justify-content-center">
            <li class="page-item">
              <a class="page-link" href="#">
                <i class="icofont-double-left"></i>
              </a>
            </li>

            <li class="page-item active">
              <a class="page-link" href="#">
                1
              </a>
            </li>

            <li class="page-item">
              <a class="page-link" href="#">
                2
              </a>
            </li>

            <li class="page-item">
              <a class="page-link" href="#">
                3
              </a>
            </li>

            <li class="page-item">
              <a class="page-link" href="#">
                <i class="icofont-double-right"></i>
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  );
};
export default ContentPagination;
